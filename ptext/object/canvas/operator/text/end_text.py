from typing import List

from ptext.object.canvas.event.end_text_event import EndTextEvent
from ptext.object.canvas.operator.canvas_operator import CanvasOperator
from ptext.primitive.pdf_object import PDFObject


class EndTextObject(CanvasOperator):
    """
    End a text object, discarding the text matrix.
    """

    def __init__(self):
        super().__init__("ET", 0)

    def invoke(self, canvas: "Canvas", operands: List[PDFObject] = []):
        canvas.graphics_state.text_matrix = None
        canvas.graphics_state.text_line_matrix = None
        canvas.event_occurred(EndTextEvent())
