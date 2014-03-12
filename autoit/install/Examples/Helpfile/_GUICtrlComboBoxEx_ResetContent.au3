#include <GuiComboBoxEx.au3>
#include <GuiImageList.au3>
#include <GUIConstantsEx.au3>
#include <WindowsConstants.au3>

$Debug_CB = False ; Check ClassName being passed to ComboBox/ComboBoxEx functions, set to True and use a handle to another control to see it work

_Main()

Func _Main()
	Local $hGUI, $hImage, $hCombo

	; Create GUI
	$hGUI = GUICreate("ComboBoxEx Reset Content", 400, 300)
	$hCombo = _GUICtrlComboBoxEx_Create($hGUI, "", 2, 2, 394, 100, BitOR($CBS_SIMPLE, $WS_VSCROLL, $WS_BORDER))
	GUISetState()

	$hImage = _GUIImageList_Create(16, 16, 5, 3)
	_GUIImageList_AddIcon($hImage, @SystemDir & "\shell32.dll", 110)
	_GUIImageList_AddIcon($hImage, @SystemDir & "\shell32.dll", 131)
	_GUIImageList_AddIcon($hImage, @SystemDir & "\shell32.dll", 165)
	_GUIImageList_AddIcon($hImage, @SystemDir & "\shell32.dll", 168)
	_GUIImageList_AddIcon($hImage, @SystemDir & "\shell32.dll", 137)
	_GUIImageList_AddIcon($hImage, @SystemDir & "\shell32.dll", 146)
	_GUIImageList_Add($hImage, _GUICtrlComboBoxEx_CreateSolidBitMap($hCombo, 0xFF0000, 16, 16))
	_GUIImageList_Add($hImage, _GUICtrlComboBoxEx_CreateSolidBitMap($hCombo, 0x00FF00, 16, 16))
	_GUIImageList_Add($hImage, _GUICtrlComboBoxEx_CreateSolidBitMap($hCombo, 0x0000FF, 16, 16))
	_GUICtrlComboBoxEx_SetImageList($hCombo, $hImage)

	_GUICtrlComboBoxEx_InitStorage($hCombo, 150, 300)

	_GUICtrlComboBoxEx_BeginUpdate($hCombo)
	For $x = 0 To 149
		_GUICtrlComboBoxEx_AddString($hCombo, StringFormat("%03d : Random string", Random(1, 100, 1)), Random(0, 8, 1), Random(0, 8, 1), Random(0, 8, 1))
	Next
	_GUICtrlComboBoxEx_EndUpdate($hCombo)

	; Reset Content
	MsgBox(4160, "Information", "Reset Content")
	_GUICtrlComboBoxEx_ResetContent($hCombo)

	Do
	Until GUIGetMsg() = $GUI_EVENT_CLOSE
EndFunc   ;==>_Main
