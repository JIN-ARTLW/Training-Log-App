#
# settings.py
#

volume_name = "Training Log App Installer"   # DMG 열었을 때 제목
format = "UDZO"                              # 압축 포맷 (일반적으로 UDZO)

# DMG 윈도우 창 크기 (왼쪽 위 좌표 (100, 100), 크기 (600, 400) 예시)
window_rect = ((100, 100), (600, 400))

app_icon = "/Users/jin-yeseo/code/project/training_log_macapp/icon.icns"

# 아이콘 크기
icon_size = 128

# /Applications 폴더에 대한 심볼릭 링크
# (자동으로 생성할 수도 있고, symlinks 딕셔너리를 명시적으로 쓸 수도 있습니다)
# applications_symlink = True
symlinks = { "Applications": "/Applications" }

# DMG 안에 넣을 파일(혹은 폴더) 목록
files = [
    "dist/Training Log.app",
]

# 아이콘 배치 위치(픽셀 단위)
icon_locations = {
    # "파일/폴더이름": (x좌표, y좌표)
    "Training Log.app": (150, 150),
    "Applications": (450, 150),
}

# 기타 설정
hide_extension = True