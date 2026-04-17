from __future__ import division
import clr
import sys
import math
clr.AddReference("System")
clr.AddReference("System.Drawing")
clr.AddReference("System.Windows.Forms")

from System.Drawing import Point, Size, SystemColors
from System.Windows.Forms import (Application, Button, Form, Label,
                                  MessageBox, TextBox, AnchorStyles,
                                  FormBorderStyle, FormStartPosition,
                                  MessageBoxButtons, MessageBoxIcon)
class EquationEditorForm(Form):
    def __init__(self, target_part):
        self.TargetPart = target_part
        self.EVAL_GLOBALS = self._create_eval_globals()
        self.Text = "Standard Function Calling"
        self.Size = Size(1280, 720)
        self.MinimumSize = Size(600, 400)
        self.FormBorderStyle = FormBorderStyle.Sizable
        self.StartPosition = FormStartPosition.CenterScreen
        self.AutoScroll = True
        self.TopMost = True # Make the form always stay on top
        self.InitializeComponents()

    def _create_eval_globals(self):
        return {
            "__builtins__": None, "pi": math.pi,
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "asin": math.asin, "acos": math.acos, "atan": math.atan,
            "sqrt": math.sqrt, "abs": abs, "int": lambda x: int(x),
            "sign": lambda x: (x > 0) - (x < 0),
            "frac": lambda x: x - math.trunc(x), "pow": pow
        }

    def InitializeComponents(self):
        all_params = self.TargetPart.Parameters
        Y_START = 15
        Y_PADDING = 10
        CONTROL_HEIGHT = 23
        X_LEFT_MARGIN = 15
        EQ_BOX_X_START = 150
        X_RIGHT_MARGIN = 15
        RESULT_BOX_WIDTH = 100
        X_PADDING = 5
        y_pos = Y_START
        for param in all_params:
            label = Label()
            label.Text = param.Name
            label.Location = Point(X_LEFT_MARGIN, y_pos + 4)
            label.AutoSize = True
            self.Controls.Add(label)
            eq_textbox = TextBox()
            eq_textbox.Location = Point(EQ_BOX_X_START, y_pos)
            eq_textbox.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right
            if param.Equation and len(param.Equation.strip()) > 0:
                eq_textbox.Text = param.Equation
            else:
                eq_textbox.Text = str(param.Value)
            self.Controls.Add(eq_textbox)
            send_button = Button()
            send_button.Text = "SEND FUNCTION RESULT TO PARAMETER"
            send_button.AutoSize = True
            send_button.Anchor = AnchorStyles.Top | AnchorStyles.Right
            send_button.Click += lambda s, e, p=param, eq=eq_textbox: self.OnSendButtonClicked(p, eq)
            self.Controls.Add(send_button)
            result_textbox = TextBox()
            result_textbox.Size = Size(RESULT_BOX_WIDTH, CONTROL_HEIGHT)
            result_textbox.Anchor = AnchorStyles.Top | AnchorStyles.Right
            result_textbox.ReadOnly = True
            result_textbox.BackColor = SystemColors.Control
            result_textbox.Text = "..."
            self.Controls.Add(result_textbox)
            eq_textbox.Tag = result_textbox
            eq_textbox.TextChanged += self.OnEquationChanged
            result_textbox.Location = Point(self.ClientSize.Width - RESULT_BOX_WIDTH - X_RIGHT_MARGIN, y_pos)
            send_button.Location = Point(result_textbox.Location.X - send_button.Width - X_PADDING, y_pos)
            eq_textbox.Size = Size(send_button.Location.X - EQ_BOX_X_START - X_PADDING, CONTROL_HEIGHT)
            self.OnEquationChanged(eq_textbox, None)
            y_pos += CONTROL_HEIGHT + Y_PADDING
        self.closeButton = Button()
        self.closeButton.Text = "Close"
        self.closeButton.Size = Size(85, 30)
        self.closeButton.Anchor = AnchorStyles.Bottom | AnchorStyles.Right
        self.closeButton.Location = Point(self.ClientSize.Width - self.closeButton.Width - X_RIGHT_MARGIN, self.ClientSize.Height - self.closeButton.Height - Y_START)
        self.closeButton.Click += lambda s, e: self.Close()
        self.Controls.Add(self.closeButton)
    def OnEquationChanged(self, sender, event_args):
        eq_textbox = sender
        result_textbox = eq_textbox.Tag
        new_text = eq_textbox.Text.strip()
        param_values = {p.Name: p.Value for p in self.TargetPart.Parameters}
        try:
            evaluated_value = eval(new_text, self.EVAL_GLOBALS, param_values)
            result_textbox.Text = "{:.4f}".format(evaluated_value)
        except:
            result_textbox.Text = "..."
    def OnSendButtonClicked(self, param_to_update, eq_textbox):
        new_text = eq_textbox.Text.strip()
        try:
            param_values = {p.Name: p.Value for p in self.TargetPart.Parameters}
            evaluated_value = eval(new_text, self.EVAL_GLOBALS, param_values)
            param_to_update.Equation = ""
            param_to_update.Value = evaluated_value
        except Exception as ex:
            MessageBox.Show("Invalid expression: '{}'\n\nError: {}".format(new_text, str(ex)),"Update Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
            return  
        self.TargetPart.Regenerate()
def main():
    Units.Current = UnitTypes.Inches
    TargetPart = CurrentPart()
    if TargetPart is None:
        MessageBox.Show("No current part window found.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error)
        return
    if not TargetPart.Parameters:
        MessageBox.Show("The current part has no parameters defined.", "Information", MessageBoxButtons.OK, MessageBoxIcon.Information)
        return
    editor_form = EquationEditorForm(TargetPart)
    Application.EnableVisualStyles()
    editor_form.ShowDialog()

main()