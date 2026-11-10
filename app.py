
import os
import gradio as gr
import numpy as np

from voice_backend import *

# --------------------------------------------------
# VOICE DEPLOYMENT INITIALIZATION
# --------------------------------------------------

def initialize_voice():

    required = [
        "VOICEApplication",
        "VOICEP300Classifier",
        "VOICE_FINAL_CONFIG",
        "VOICE_FINAL_GRID",
        "VOICEMessagingEngine",
        "VOICESessionManager",
        "VOICEErrorRecovery"
    ]

    missing = [name for name in required if name not in globals()]

    if missing:
        raise RuntimeError(
            "Missing backend components: " + ", ".join(missing)
        )

    raise RuntimeError(
        "Deployment initialization needs the trained classifier "
        "and its saved model. Connect those before launching."
    )


# --------------------------------------------------
# GRADIO INTERFACE
# --------------------------------------------------

with gr.Blocks(title="VOICE | Adaptive EEG Communication") as demo:

    gr.Markdown(
        """
        # VOICE
        ### Adaptive EEG Communication System

        P300-based character selection and communication.
        """
    )

    status = gr.Markdown(
        "⚠️ Backend initialization pending."
    )

    message = gr.Textbox(
        label="Composed message",
        lines=4,
        interactive=True
    )

    gr.Markdown("### Character Grid")

    grid = gr.Dataframe(
        value=VOICE_FINAL_GRID if "VOICE_FINAL_GRID" in globals()
        else [list("ABCDEF"), list("GHIJKL"), list("MNOPQR"),
              list("STUVWX"), list("YZ0123"), list("456789")],
        interactive=False,
        headers=None,
        row_count=6,
        col_count=6
    )

    gr.Markdown(
        "The EEG decoder and session controls will be enabled "
        "after the trained model is connected."
    )

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 10000))
    )
