import streamlit as st
import boto3
import os

# --- S3 Configuration ---
BUCKET_NAME = "ppe-detection-input-v1"  # 你自己的 S3 bucket 名
UPLOAD_PREFIX = "s3-sample-images/"           # 上传路径前缀

# --- Streamlit 页面设置 ---
st.set_page_config(page_title="AI-powered PPE Detection", page_icon="🦺", layout="centered")
st.title("🦺 AI-powered PPE Detection")
st.markdown("Upload a photo to detect PPE using AWS Rekognition.")

# --- 上传图像控件 ---
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    if st.button("Upload & Detect"):
        # 保存临时文件
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        # 上传到 S3
        try:
            s3 = boto3.client("s3")
            s3.upload_file(
                Filename=uploaded_file.name,
                Bucket=BUCKET_NAME,
                Key=UPLOAD_PREFIX + uploaded_file.name
            )
            st.success(f"✅ Uploaded to S3 bucket `{BUCKET_NAME}` successfully!")
        except Exception as e:
            st.error(f"❌ Failed to upload to S3: {e}")
            st.stop()

        # 读取图像二进制并调用 Rekognition
        try:
            with open(uploaded_file.name, "rb") as image_file:
                image_bytes = image_file.read()

            rekognition = boto3.client("rekognition")
            response = rekognition.detect_protective_equipment(
                Image={'Bytes': image_bytes},
                SummarizationAttributes={
                    'MinConfidence': 80.0,
                    'RequiredEquipmentTypes': ['HEAD_COVER', 'FACE_COVER', 'HAND_COVER']
                }
            )

            # 显示原始 JSON
            st.subheader("🔍 Raw Rekognition Response")
            st.json(response)

            # 显示简化结果
            st.subheader("🧠 Simplified PPE Detection Result")
            persons = response.get("Persons", [])
            if not persons:
                st.warning("No person detected in the image.")
            for idx, person in enumerate(persons):
                st.markdown(f"**👤 Person {idx+1}**")
                for body_part in person.get("BodyParts", []):
                    name = body_part.get("Name")
                    equipment = body_part.get("EquipmentDetections", [])
                    if not equipment:
                        st.write(f"- {name}: ❌ No PPE detected")
                    else:
                        for eq in equipment:
                            eq_type = eq["Type"]
                            confidence = eq["Confidence"]
                            covers = eq["CoversBodyPart"]["Value"]
                            st.write(f"- {eq_type} on {name}: {'✅ Yes' if covers else '❌ No'} ({confidence:.1f}%)")

        except Exception as e:
            st.error(f"❌ Rekognition detection failed: {e}")
