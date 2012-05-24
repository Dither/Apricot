# -*- coding: utf-8 -*-
# Settings.py
# Copyright © Masaaki Kawata All rights reserved.

import clr
clr.AddReferenceByPartialName("mscorlib")
clr.AddReferenceByPartialName("System")
clr.AddReferenceByPartialName("System.Configuration")
clr.AddReferenceByPartialName("System.Xml")
clr.AddReferenceByPartialName("PresentationCore")
clr.AddReferenceByPartialName("PresentationFramework")
clr.AddReferenceByPartialName("Apricot")

from System import String, Boolean, Int32, Int64, Double, Convert, Type, Environment, GC
from System.IO import File, Directory, FileInfo, DirectoryInfo, Path
from System.Collections.Generic import List
from System.Configuration import ConfigurationManager, ConfigurationUserLevel, ExeConfigurationFileMap, ConfigurationSaveMode
from System.Diagnostics import Process, ProcessStartInfo
from System.Globalization import CultureInfo
from System.Reflection import Assembly
from System.Threading.Tasks import Task
from System.Windows import Application, Window, FontSizeConverter, HorizontalAlignment, VerticalAlignment, Thickness, RoutedEventHandler
from System.Windows.Controls import MenuItem, Separator, StackPanel, TextBox, Button, Orientation
from System.Xml import XmlDocument, XmlNode, XmlAttribute, XmlNodeType
from Apricot import Script

program = "notepad.exe"

def onOpened(s, e):
	global menuItem

	menuItem.Items.Clear()

	learningMenuItem = MenuItem()
	updateMenuItem = MenuItem()
	
	stackPanel = StackPanel()
	stackPanel.HorizontalAlignment = HorizontalAlignment.Left
	stackPanel.VerticalAlignment = VerticalAlignment.Top
	stackPanel.Orientation = Orientation.Horizontal
	
	textBox = TextBox()
	textBox.Width = 240
	
	def onMouseUp(sender, mbea):
		mbea.Handled = True
			
	def onKeyDown(sender, kea):
		kea.Handled = True
		
	textBox.MouseUp += onMouseUp
	updateMenuItem.KeyDown += onKeyDown
	
	button = Button()
	button.Margin = Thickness(10, 0, 0, 0)
	button.Padding = Thickness(5, 0, 5, 0)
	button.IsDefault = True
	
	if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
		learningMenuItem.Header = "言葉を教える"
		button.Content = "教える"
	else:
		learningMenuItem.Header = "Learning"
		button.Content = "Learn"
		
	def onClick(sender, rea):
		if not String.IsNullOrEmpty(textBox.Text):
			Script.Instance.Learn(textBox.Text)
	
	button.Click += onClick
	
	stackPanel.Children.Add(textBox)
	stackPanel.Children.Add(button)
	
	updateMenuItem.Header = stackPanel
	learningMenuItem.Items.Add(updateMenuItem)
	menuItem.Items.Add(learningMenuItem)
	menuItem.Items.Add(Separator())

	config = None
	directoryInfo = DirectoryInfo(Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData), Assembly.GetExecutingAssembly().GetName().Name))
	
	if directoryInfo.Exists:
		fileName = Path.GetFileName(Assembly.GetExecutingAssembly().Location)
		
		for fileInfo in directoryInfo.EnumerateFiles("*.config"):
			if fileName.Equals(Path.GetFileNameWithoutExtension(fileInfo.Name)):
				exeConfigurationFileMap = ExeConfigurationFileMap()
				
				exeConfigurationFileMap.ExeConfigFilename = fileInfo.FullName
				config = ConfigurationManager.OpenMappedExeConfiguration(exeConfigurationFileMap, ConfigurationUserLevel.None)
	
	if config == None:
		config = ConfigurationManager.OpenExeConfiguration(ConfigurationUserLevel.None)
		directoryInfo = None

	if config.HasFile:
		if config.AppSettings.Settings["ActivateThreshold"] != None:
			threshold = Int64.Parse(config.AppSettings.Settings["ActivateThreshold"].Value)
			
			childMenuItem = MenuItem()
			
			if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
				childMenuItem.Header = "トーク間隔"
			else:
				childMenuItem.Header = "Talking Interval"

			intervalMenuItem1 = MenuItem()
			
			if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
				intervalMenuItem1.Header = "15秒"
			else:
				intervalMenuItem1.Header = "15 seconds"
			
			if threshold == 150000000:
				intervalMenuItem1.IsChecked = True
				
			def onIntervalClick1(sender, args):
				config.AppSettings.Settings["ActivateThreshold"].Value = "150000000"
				config.Save(ConfigurationSaveMode.Modified)
			
			intervalMenuItem1.Click += onIntervalClick1
					
			childMenuItem.Items.Add(intervalMenuItem1)
			
			intervalMenuItem2 = MenuItem()
			
			if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
				intervalMenuItem2.Header = "30秒"
			else:
				intervalMenuItem2.Header = "30 seconds"
			
			if threshold == 300000000:
				intervalMenuItem2.IsChecked = True
				
			def onIntervalClick2(sender, args):
				config.AppSettings.Settings["ActivateThreshold"].Value = "300000000"
				config.Save(ConfigurationSaveMode.Modified)
			
			intervalMenuItem2.Click += onIntervalClick2
					
			childMenuItem.Items.Add(intervalMenuItem2)
			
			intervalMenuItem3 = MenuItem()
			
			if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
				intervalMenuItem3.Header = "1分"
			else:
				intervalMenuItem3.Header = "1 minute"
			
			if threshold == 600000000:
				intervalMenuItem3.IsChecked = True
				
			def onIntervalClick3(sender, args):
				config.AppSettings.Settings["ActivateThreshold"].Value = "600000000"
				config.Save(ConfigurationSaveMode.Modified)
			
			intervalMenuItem3.Click += onIntervalClick3
					
			childMenuItem.Items.Add(intervalMenuItem3)

			intervalMenuItem4 = MenuItem()
			
			if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
				intervalMenuItem4.Header = "2分"
			else:
				intervalMenuItem4.Header = "2 minutes"
			
			if threshold == 1200000000:
				intervalMenuItem4.IsChecked = True
				
			def onIntervalClick4(sender, args):
				config.AppSettings.Settings["ActivateThreshold"].Value = "1200000000"
				config.Save(ConfigurationSaveMode.Modified)
			
			intervalMenuItem4.Click += onIntervalClick4
					
			childMenuItem.Items.Add(intervalMenuItem4)

			intervalMenuItem5 = MenuItem()
			
			if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
				intervalMenuItem5.Header = "3分"
			else:
				intervalMenuItem5.Header = "3 minutes"
			
			if threshold == 1800000000:
				intervalMenuItem5.IsChecked = True
				
			def onIntervalClick5(sender, args):
				config.AppSettings.Settings["ActivateThreshold"].Value = "1800000000"
				config.Save(ConfigurationSaveMode.Modified)
			
			intervalMenuItem5.Click += onIntervalClick5
					
			childMenuItem.Items.Add(intervalMenuItem5)
			
			menuItem.Items.Add(childMenuItem)
			
		menuItem.Items.Add(Separator())
		
		childMenuItem = MenuItem()
		
		if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
			childMenuItem.Header = "テーマ"
		else:
			childMenuItem.Header = "Theme"

		menuItem1 = MenuItem()
		menuItem2 = MenuItem()
		menuItem3 = MenuItem()
		menuItem4 = MenuItem()
		menuItem5 = MenuItem()
		menuItem6 = MenuItem()
		menuItem7 = MenuItem()
		menuItem8 = MenuItem()
		menuItem9 = MenuItem()
		menuItem10 = MenuItem()
		
		if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
			menuItem1.Header = "ブループリント"
			menuItem2.Header = "ドット1"
			menuItem3.Header = "ドット2"
			menuItem4.Header = "リンネル"
			menuItem5.Header = "ノイズ1"
			menuItem6.Header = "ノイズ2"
			menuItem7.Header = "ノイズ3"
			menuItem8.Header = "ペーパー"
			menuItem9.Header = "ストライプ1"
			menuItem10.Header = "ストライプ2"
		else:
			menuItem1.Header = "Blueprint"
			menuItem2.Header = "Dots 1"
			menuItem3.Header = "Dots 2"
			menuItem4.Header = "Linen"
			menuItem5.Header = "Noize 1"
			menuItem6.Header = "Noize 2"
			menuItem7.Header = "Noize 3"
			menuItem8.Header = "Paper"
			menuItem9.Header = "Stripes 1"
			menuItem10.Header = "Stripes 2"
		
		if config.AppSettings.Settings["BackgroundColor"] != None and config.AppSettings.Settings["BackgroundImage"] != None and config.AppSettings.Settings["TextColor"] != None and config.AppSettings.Settings["LinkColor"]:
			backColor = config.AppSettings.Settings["BackgroundColor"].Value
			backImage = config.AppSettings.Settings["BackgroundImage"].Value
			textColor = config.AppSettings.Settings["TextColor"].Value
			linkColor = config.AppSettings.Settings["LinkColor"].Value

			if backColor.Equals("#FF2574B0") and backImage.Equals("Assets\\Background-Blueprint.png") and textColor.Equals("#FFFFFFFF") and linkColor.Equals("#FFFEEC27"):
				menuItem1.IsChecked = True
				
			def onClick1(sender, args):
				config.AppSettings.Settings["BackgroundColor"].Value = "#FF2574B0"
				config.AppSettings.Settings["BackgroundImage"].Value = "Assets\\Background-Blueprint.png"
				config.AppSettings.Settings["TextColor"].Value = "#FFFFFFFF"
				config.AppSettings.Settings["LinkColor"].Value = "#FFFEEC27"
				config.Save(ConfigurationSaveMode.Modified)
			
			menuItem1.Click += onClick1

			if backColor.Equals("#FF3B3F41") and backImage.Equals("Assets\\Background-Dots1.png") and textColor.Equals("#FFFFFFFF") and linkColor.Equals("#FFF26C4F"):
				menuItem2.IsChecked = True
				
			def onClick2(sender, args):
				config.AppSettings.Settings["BackgroundColor"].Value = "#FF3B3F41"
				config.AppSettings.Settings["BackgroundImage"].Value = "Assets\\Background-Dots1.png"
				config.AppSettings.Settings["TextColor"].Value = "#FFFFFFFF"
				config.AppSettings.Settings["LinkColor"].Value = "#FFF26C4F"
				config.Save(ConfigurationSaveMode.Modified)
			
			menuItem2.Click += onClick2

			if backColor.Equals("#FF252525") and backImage.Equals("Assets\\Background-Dots2.png") and textColor.Equals("#FFFFFFFF") and linkColor.Equals("#FF00C0FF"):
				menuItem3.IsChecked = True
				
			def onClick3(sender, args):
				config.AppSettings.Settings["BackgroundColor"].Value = "#FF252525"
				config.AppSettings.Settings["BackgroundImage"].Value = "Assets\\Background-Dots2.png"
				config.AppSettings.Settings["TextColor"].Value = "#FFFFFFFF"
				config.AppSettings.Settings["LinkColor"].Value = "#FF00C0FF"
				config.Save(ConfigurationSaveMode.Modified)
			
			menuItem3.Click += onClick3

			if backColor.Equals("#FF252525") and backImage.Equals("Assets\\Background-Linen.png") and textColor.Equals("#FFFFFFFF") and linkColor.Equals("#FFFF6600"):
				menuItem4.IsChecked = True
				
			def onClick4(sender, args):
				config.AppSettings.Settings["BackgroundColor"].Value = "#FF252525"
				config.AppSettings.Settings["BackgroundImage"].Value = "Assets\\Background-Linen.png"
				config.AppSettings.Settings["TextColor"].Value = "#FFFFFFFF"
				config.AppSettings.Settings["LinkColor"].Value = "#FFFF6600"
				config.Save(ConfigurationSaveMode.Modified)
			
			menuItem4.Click += onClick4
			
			if backColor.Equals("#FFF2F2F2") and backImage.Equals("Assets\\Background-Noize1.png") and textColor.Equals("#FF000000") and linkColor.Equals("#FFFF0099"):
				menuItem5.IsChecked = True
				
			def onClick5(sender, args):
				config.AppSettings.Settings["BackgroundColor"].Value = "#FFF2F2F2"
				config.AppSettings.Settings["BackgroundImage"].Value = "Assets\\Background-Noize1.png"
				config.AppSettings.Settings["TextColor"].Value = "#FF000000"
				config.AppSettings.Settings["LinkColor"].Value = "#FFFF0099"
				config.Save(ConfigurationSaveMode.Modified)
			
			menuItem5.Click += onClick5
			
			if backColor.Equals("#FFE5E5E5") and backImage.Equals("Assets\\Background-Noize2.png") and textColor.Equals("#FF333333") and linkColor.Equals("#FFFF6600"):
				menuItem6.IsChecked = True
				
			def onClick6(sender, args):
				config.AppSettings.Settings["BackgroundColor"].Value = "#FFE5E5E5"
				config.AppSettings.Settings["BackgroundImage"].Value = "Assets\\Background-Noize2.png"
				config.AppSettings.Settings["TextColor"].Value = "#FF333333"
				config.AppSettings.Settings["LinkColor"].Value = "#FFFF6600"
				config.Save(ConfigurationSaveMode.Modified)
			
			menuItem6.Click += onClick6

			if backColor.Equals("#FF34383E") and backImage.Equals("Assets\\Background-Noize3.png") and textColor.Equals("#FFFFFFFF") and linkColor.Equals("#FFFF6600"):
				menuItem7.IsChecked = True
				
			def onClick7(sender, args):
				config.AppSettings.Settings["BackgroundColor"].Value = "#FF34383E"
				config.AppSettings.Settings["BackgroundImage"].Value = "Assets\\Background-Noize3.png"
				config.AppSettings.Settings["TextColor"].Value = "#FFFFFFFF"
				config.AppSettings.Settings["LinkColor"].Value = "#FFFF6600"
				config.Save(ConfigurationSaveMode.Modified)
			
			menuItem7.Click += onClick7

			if backColor.Equals("#FFFCFCFC") and backImage.Equals("Assets\\Background-Paper.png") and textColor.Equals("#FF000000") and linkColor.Equals("#FFDD1A00"):
				menuItem8.IsChecked = True
				
			def onClick8(sender, args):
				config.AppSettings.Settings["BackgroundColor"].Value = "#FFFCFCFC"
				config.AppSettings.Settings["BackgroundImage"].Value = "Assets\\Background-Paper.png"
				config.AppSettings.Settings["TextColor"].Value = "#FF000000"
				config.AppSettings.Settings["LinkColor"].Value = "#FFDD1A00"
				config.Save(ConfigurationSaveMode.Modified)
			
			menuItem8.Click += onClick8

			if backColor.Equals("#FF70D0E7") and backImage.Equals("Assets\\Background-Stripes1.png") and textColor.Equals("#FFFFFFFF") and linkColor.Equals("#FFFF6600"):
				menuItem9.IsChecked = True
				
			def onClick9(sender, args):
				config.AppSettings.Settings["BackgroundColor"].Value = "#FF70D0E7"
				config.AppSettings.Settings["BackgroundImage"].Value = "Assets\\Background-Stripes1.png"
				config.AppSettings.Settings["TextColor"].Value = "#FFFFFFFF"
				config.AppSettings.Settings["LinkColor"].Value = "#FFFF6600"
				config.Save(ConfigurationSaveMode.Modified)
			
			menuItem9.Click += onClick9

			if backColor.Equals("#FF39343D") and backImage.Equals("Assets\\Background-Stripes2.png") and textColor.Equals("#FFFFFFFF") and linkColor.Equals("#FFFF6600"):
				menuItem10.IsChecked = True
				
			def onClick10(sender, args):
				config.AppSettings.Settings["BackgroundColor"].Value = "#FF39343D"
				config.AppSettings.Settings["BackgroundImage"].Value = "Assets\\Background-Stripes2.png"
				config.AppSettings.Settings["TextColor"].Value = "#FFFFFFFF"
				config.AppSettings.Settings["LinkColor"].Value = "#FFFF6600"
				config.Save(ConfigurationSaveMode.Modified)
			
			menuItem10.Click += onClick10
		
		childMenuItem.Items.Add(menuItem1)
		childMenuItem.Items.Add(menuItem2)
		childMenuItem.Items.Add(menuItem3)
		childMenuItem.Items.Add(menuItem4)
		childMenuItem.Items.Add(menuItem5)
		childMenuItem.Items.Add(menuItem6)
		childMenuItem.Items.Add(menuItem7)
		childMenuItem.Items.Add(menuItem8)
		childMenuItem.Items.Add(menuItem9)
		childMenuItem.Items.Add(menuItem10)
		menuItem.Items.Add(childMenuItem)
		
		if config.AppSettings.Settings["DropShadow"] != None:
			dropShadow = Boolean.Parse(config.AppSettings.Settings["DropShadow"].Value)
			
			childMenuItem = MenuItem()
			childMenuItem.IsChecked = dropShadow
			
			if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
				childMenuItem.Header = "ドロップシャドウを有効にする"
			else:
				childMenuItem.Header = "Enable Drop Shadow"
			
			def onClick(sender, args):
				config.AppSettings.Settings["DropShadow"].Value = (not sender.IsChecked).ToString()
				config.Save(ConfigurationSaveMode.Modified)
			
			childMenuItem.Click += onClick
			
			menuItem.Items.Add(Separator())
			menuItem.Items.Add(childMenuItem)
		
		menuItem.Items.Add(Separator())
			
		if config.AppSettings.Settings["FontFamily"] != None:
			fontFamilyName = config.AppSettings.Settings["FontFamily"].Value
			
			childMenuItem = MenuItem()
			
			if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
				childMenuItem.Header = "フォント"
			else:
				childMenuItem.Header = "Font"
				
			for fontFamily in ["Arial", "Calibri", "Cambria", "Candara", "Constantia", "Corbel", "Courier New", "Geogia", "MS UI Gothic", "Segoe UI", "Tahoma", "Times New Roman", "Verdana", "メイリオ", "ＭＳ ゴシック"]:
				fontMenuItem = MenuItem()
				fontMenuItem.Header = fontFamily
			
				if fontFamily.Equals(fontFamilyName):
					fontMenuItem.IsChecked = True
					
				def onClick(sender, args):
					config.AppSettings.Settings["FontFamily"].Value = sender.Header
					config.Save(ConfigurationSaveMode.Modified)
				
				fontMenuItem.Click += onClick
			
				childMenuItem.Items.Add(fontMenuItem)
			
			menuItem.Items.Add(childMenuItem)
			
		if config.AppSettings.Settings["FontSize"] != None:
			fontSize = config.AppSettings.Settings["FontSize"].Value
			
			fontSizeConverter = FontSizeConverter()
			childMenuItem = MenuItem()
			
			if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
				childMenuItem.Header = "フォントサイズ"
			else:
				childMenuItem.Header = "Font Size"
			
			for size in ["8pt", "9pt", "10pt", "11pt", "12pt", "14pt", "16pt", "18pt", "20pt", "22pt", "24pt"]:
				fontMenuItem = MenuItem()
				fontMenuItem.Header = size
				
				if fontSize.Equals(size):
					fontMenuItem.IsChecked = True
					
				def onClick(sender, args):
					config.AppSettings.Settings["FontSize"].Value = sender.Header
					config.Save(ConfigurationSaveMode.Modified)
				
				fontMenuItem.Click += onClick
				
				childMenuItem.Items.Add(fontMenuItem)
				
			menuItem.Items.Add(childMenuItem)
				
			if config.AppSettings.Settings["LineHeight"] != None:
				lineHeight = Double.Parse(config.AppSettings.Settings["LineHeight"].Value)
				maxLineHeight = Convert.ToInt32(fontSizeConverter.ConvertFromString(fontSize)) * 2
				
				if maxLineHeight < lineHeight:
					maxLineHeight = lineHeight
				
				childMenuItem2 = MenuItem()
				
				if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
					childMenuItem2.Header = "行間"
				else:
					childMenuItem2.Header = "Line Height"
				
				for i in range(Convert.ToInt32(fontSizeConverter.ConvertFromString(fontSize)), Convert.ToInt32(maxLineHeight) + 1):
					lineHeightMenuItem = MenuItem()
					lineHeightMenuItem.Header = i.ToString()
					
					if lineHeight == i:
						lineHeightMenuItem.IsChecked = True
						
					def onClick(sender, args):
						config.AppSettings.Settings["LineHeight"].Value = sender.Header
						config.Save(ConfigurationSaveMode.Modified)
					
					lineHeightMenuItem.Click += onClick
					
					childMenuItem2.Items.Add(lineHeightMenuItem)
			
				menuItem.Items.Add(childMenuItem2)
				
		if config.AppSettings.Settings["FrameRate"] != None:
			frameRate = Double.Parse(config.AppSettings.Settings["FrameRate"].Value)
			
			childMenuItem = MenuItem()
			
			if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
				childMenuItem.Header = "フレームレート"
			else:
				childMenuItem.Header = "Frame Rate"
			
			for i in [24, 30, 60]:
				frameRateMenuItem = MenuItem()
				frameRateMenuItem.Header = i.ToString()
				
				if frameRate == Convert.ToDouble(i):
					frameRateMenuItem.IsChecked = True
					
				def onClick(sender, args):
					config.AppSettings.Settings["FrameRate"].Value = sender.Header
					config.Save(ConfigurationSaveMode.Modified)
				
				frameRateMenuItem.Click += onClick
				
				childMenuItem.Items.Add(frameRateMenuItem)
			
			menuItem.Items.Add(Separator())
			menuItem.Items.Add(childMenuItem)

		if config.AppSettings.Settings["Subscriptions"] != None:
			path = config.AppSettings.Settings["Subscriptions"].Value
			
			childMenuItem = MenuItem()
			
			if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
				childMenuItem.Header = "フィード"
			else:
				childMenuItem.Header = "Subscriptions"
			
			editMenuItem = MenuItem()
			editMenuItem.Tag = path
			
			def onEdit(sender, args):
				global program
				
				path = sender.Tag

				def onStart(state):
					Process.Start(state)
					
				psi = ProcessStartInfo()

				if String.IsNullOrEmpty(program):
					psi.FileName = path
				else:
					psi.FileName = program
					psi.Arguments = path
				
				Task.Factory.StartNew(onStart, psi)
			
			editMenuItem.Click += onEdit
			
			if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
				editMenuItem.Header = "フィードの編集..."
			else:
				editMenuItem.Header = "Edit..."
			
			childMenuItem.Items.Add(editMenuItem)
			childMenuItem.Items.Add(Separator())
			
			if directoryInfo != None:
				fileInfo = FileInfo(Path.Combine(directoryInfo.FullName, path))
			
				if fileInfo.Exists:
					path = fileInfo.FullName
					
			def parseOutline(m, n):
				if not n.HasChildNodes:
					return None

				for xmlNode in n.ChildNodes:
					if xmlNode.Name.Equals("outline"):
						text = None
						xmlUrl = None
						htmlUrl = None

						for xmlAttribute in xmlNode.Attributes:
							if xmlAttribute.Name.Equals("title") or xmlAttribute.Name.Equals("text"):
								text = xmlAttribute.Value
							elif xmlAttribute.Name.Equals("xmlUrl"):
								xmlUrl = xmlAttribute.Value
							elif xmlAttribute.Name.Equals("htmlUrl"):
								htmlUrl = xmlAttribute.Value
						
						if not String.IsNullOrEmpty(text):
							if String.IsNullOrEmpty(xmlUrl):
								mi = MenuItem()
								mi.Header = text
								
								parsedMenuItem = parseOutline(mi, xmlNode)
								
								if parsedMenuItem == None:
									m.Items.Add(mi)
								else:
									m.Items.Add(parsedMenuItem)
							elif not String.IsNullOrEmpty(xmlUrl):
								mi = MenuItem()
								
								def onClick(sender, args):
									if not String.IsNullOrEmpty(sender.Tag):
										def onStart(state):
											Process.Start(state)

										Task.Factory.StartNew(onStart, sender.Tag)
								
								mi.Header = text
								mi.Click += onClick
								mi.Tag = htmlUrl
								
								m.Items.Add(mi)
				
				return m
				
			doc = XmlDocument()
			doc.Load(path)

			for xmlNode in doc.SelectNodes("/opml/body"):
				parseOutline(childMenuItem, xmlNode)
			
			menuItem.Items.Add(Separator())
			menuItem.Items.Add(childMenuItem)

		if config.AppSettings.Settings["Timeout"] != None:
			timeout = Int32.Parse(config.AppSettings.Settings["Timeout"].Value)
			
			childMenuItem = MenuItem()
			
			if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
				childMenuItem.Header = "タイムアウト"
			else:
				childMenuItem.Header = "Timeout"
			
			for i in [15000, 30000, 60000, 120000, 180000]:
				timeMenuItem = MenuItem()
				timeMenuItem.Header = i.ToString()
				
				if timeout == i:
					timeMenuItem.IsChecked = True
					
				def onClick(sender, args):
					config.AppSettings.Settings["Timeout"].Value = sender.Header
					config.Save(ConfigurationSaveMode.Modified)
				
				timeMenuItem.Click += onClick
				
				childMenuItem.Items.Add(timeMenuItem)
			
			menuItem.Items.Add(Separator())
			menuItem.Items.Add(childMenuItem)

		if config.AppSettings.Settings["Cache"] != None:
			path = config.AppSettings.Settings["Cache"].Value
			
			if directoryInfo != None:
				path = Path.Combine(directoryInfo.FullName, path)
				
			childMenuItem = MenuItem()
			childMenuItem.Tag = path
			
			if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
				childMenuItem.Header = "キャッシュをクリア"
			else:
				childMenuItem.Header = "Clear Cache"
				
			def onClick(sender, args):
				if Directory.Exists(childMenuItem.Tag):
					for fileName in Directory.GetFiles(childMenuItem.Tag):
						File.Delete(fileName)
			
			childMenuItem.Click += onClick
			
			menuItem.Items.Add(Separator())
			menuItem.Items.Add(childMenuItem)
		
		childMenuItem = MenuItem()
		
		if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
			childMenuItem.Header = "GCを強制的に実行"
		else:
			childMenuItem.Header = "Force Garbage Collection"
			
		def onClick(sender, args):
			GC.Collect()
		
		childMenuItem.Click += onClick
		
		menuItem.Items.Add(childMenuItem)

def onKeyDown(s, e):
	e.Handled = False

def onStart(s, e):
	global menuItem, separator
	
	for window in Application.Current.Windows:
		if window == Application.Current.MainWindow and window.ContextMenu != None:
			if not window.ContextMenu.Items.Contains(menuItem):
				window.ContextMenu.Opened += onOpened
				window.ContextMenu.Items.Insert(window.ContextMenu.Items.Count - 4, menuItem)
				window.ContextMenu.AddHandler(Button.KeyDownEvent, RoutedEventHandler(onKeyDown), True)
				
				if not clr.GetClrType(Separator).IsInstanceOfType(window.ContextMenu.Items[10]):
					separator = Separator()
					window.ContextMenu.Items.Insert(10, separator)

menuItem = MenuItem()
separator = None

if CultureInfo.CurrentCulture.Equals(CultureInfo.GetCultureInfo("ja-JP")):
	menuItem.Header = "オプション"
else:
	menuItem.Header = "Settings"

Script.Instance.Start += onStart