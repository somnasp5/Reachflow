
import os

from fastapi import (
    APIRouter,
    Form,
    UploadFile,
    File
)

from app.services.email_sender_service import (
    send_email
)

router = APIRouter()


@router.post("/send-email")
async def send_email_route(

    receiver_email: str = Form(...),

    subject: str = Form(...),

    body: str = Form(...),

    attachment: UploadFile = File(None)
):

    attachment_path = None

    # SAVE ATTACHMENT

    if attachment:

        os.makedirs(
            "temp_uploads",
            exist_ok=True
        )

        attachment_path = (
            f"temp_uploads/{attachment.filename}"
        )

        with open(
            attachment_path,
            "wb"
        ) as f:

            f.write(
                await attachment.read()
            )

    # SEND EMAIL

    send_email(

        receiver_email=receiver_email,

        subject=subject,

        body=body,

        attachment_path=attachment_path
    )

    return {
        "success": True,
        "message": "Email Sent Successfully"
    }
