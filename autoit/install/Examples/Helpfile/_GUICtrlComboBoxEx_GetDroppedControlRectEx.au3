#include <GuiComboBoxEx.au3>
#include <GUIConstantsEx.au3>
#include <Constants.au3>

$Debug_CB = False ; Check ClassName being passed to ComboBox/ComboBoxEx functions, set to True and use a handle to another control to see it work

_Main()

Func _Main()
	Local $hGUI, $tRect, $hCombo

	; Create GUI
	$hGUI = GUICreate("ComboBoxEx Get Dropped Control RectEx", 400, 300)
	$hCombo = _GUICtrlComboBoxEx_Create($hGUI, "", 2, 2, 394, 100)
	GUISetState()

	; Add files
	_GUICtrlComboBoxEx_BeginUpdate($hCombo)
	_GUICtrlComboBoxEx_AddDir($hCombo, "", $DDL_DRIVES, False)
	_GUICtrlComboBoxEx_AddDir($hCombo, "", $DDL_DRIVES)
	_GUICtrlComboBoxEx_BeginUpdate($hCombo)
	_GUICtrlComboBoxEx_AddDir($hCombo, @WindowsDir & "\*.exe")
	_GUICtrlComboBoxEx_EndUpdate($hCombo)
	_GUICtrlComboBoxEx_EndUpdate($hCombo)

	; Get Dropped Control Rect
	$tRect = _GUICtrlComboBoxEx_GetDroppedControlRectEx($hCombo)
	MsgBox(4160, "Information", "Dropped Control Rect: " & _
			StringFormat("[%d][%d][%d][%d]", DllStructGetData($tRect, "Left"), DllStructGetData($tRect, "Top"), _
			DllStructGetData($tRect, "Right"), DllStructGetData($tRect, "Bottom")))

	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE
EndFunc   ;==>_Main
