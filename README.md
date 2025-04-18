<svg width="100" height="100" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="clockFaceGradient" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" style="stop-color:#B0E0E6;stop-opacity:1" /><stop offset="100%" style="stop-color:#FFFFFF;stop-opacity:1" /></linearGradient><filter id="dropShadow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur in="SourceAlpha" stdDeviation="2.5"/><feOffset dx="2" dy="4" result="offsetblur"/><feComponentTransfer><feFuncA type="linear" slope="0.4"/></feComponentTransfer><feMerge><feMergeNode in="offsetblur"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><g filter="url(#dropShadow)"><circle cx="50" cy="47" r="40" fill="url(#clockFaceGradient)" stroke="#778899" stroke-width="1.5"/><circle cx="50" cy="47" r="2.5" fill="#2F4F4F"/><line x1="50" y1="47" x2="38" y2="40" stroke="#2F4F4F" stroke-width="3.5" stroke-linecap="round"/><line x1="50" y1="47" x2="65" y2="28" stroke="#2F4F4F" stroke-width="2.5" stroke-linecap="round"/></g></svg>
# FloatClock - 悬浮计时器

FloatClock 是一个简洁、优雅且始终置顶的桌面悬浮计时器应用。它以无边框、透明背景的形式显示经过的时间，让您可以专注于任务而不受干扰。
## 主要特性
*   **始终置顶**: 窗口总是在其他窗口之上，方便随时查看。
*   **简洁无边框**: 没有传统窗口的标题栏和边框，界面干净。
*   **透明背景**: `lightgray` 颜色被设置为透明，只有时间数字可见。
*   **可拖动**: 点击并拖动时间显示区域，可以将其移动到屏幕的任何位置。
*   **清晰的时间显示**: 以 `MM:SS` (分钟:秒) 格式显示计时。
*   **自定义外观**:
    *   可以轻松设置字体颜色（`font_color`）。
    *   可以设置文字轮廓颜色（`outline_color`），增强可读性。
    *   字体、字号、粗细可在代码内修改 (`font_family`, `font_size`, `font_weight`)。
*   **悬停控制**: 鼠标悬停在计时器上时，会显示控制按钮：
    *   **暂停/继续**: 切换计时器的运行状态。
    *   **重新计时**: 将计时器重置为 0 并开始计时。
    *   **退出**: 关闭应用程序（会弹出确认对话框）。
*   **退出确认**: 在退出前会进行确认，防止误操作。
## 如何使用
1.  **运行脚本**: 使用 Python 运行提供的 `.py` 脚本。<br>
    **运行程序**: 直接双击运行`FloatClock-1.0.exe`程序。
2.  **自动开始**: 计时器窗口出现并自动开始计时。 
4.  **移动窗口**: 点击并拖动时间数字来移动窗口位置。 
6.  **访问控制**: 将鼠标指针移动到时间数字上，控制按钮（暂停、重新计时、退出）将自动出现。
8.  **操作**: 点击相应的按钮来控制计时器或退出程序。
## 自定义示例
在创建 `FloatingTimer` 实例时，可以传递颜色参数：
```python
# 使用红色字体和白色轮廓（如代码中示例）
timer_app = FloatingTimer(root, font_color="red", outline_color="white")
# 使用蓝色字体和黄色轮廓
# timer_app = FloatingTimer(root, font_color="blue", outline_color="yellow")

##依赖
#Python 3: 需要 Python 3 环境。
#Tkinter: Python 的标准 GUI 库，通常随 Python 一起安装。
#(可选) winsound: 代码中导入了 winsound 模块（用于播放系统声音），但这在当前计时器功能中并未使用。如果未来添加声音提示功能，则仅在 Windows 上有效。
