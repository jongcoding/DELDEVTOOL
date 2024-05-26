import winreg
import os
import subprocess
import ctypes

def disable_ie_dev():
    try:
        # HKEY_LOCAL_MACHINE 경로 설정
        ie_registry_paths = [
            r"SOFTWARE\Policies\Microsoft\Internet Explorer\IEDevTools",
            r"SOFTWARE\WOW6432Node\Policies\Microsoft\Internet Explorer\IEDevTools",
            r"SOFTWARE\Policies\Microsoft\Internet Explorer\Restrictions",
            r"SOFTWARE\WOW6432Node\Policies\Microsoft\Internet Explorer\Restrictions"
        ]

        for ie_path in ie_registry_paths:
            # 레지스트리 키 추가
            ie_registry_key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, ie_path)
            winreg.SetValueEx(ie_registry_key, "Disabled", 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(ie_registry_key)

        # HKEY_CURRENT_USER 경로 설정
        ie_registry_paths_current_user = [
            r"SOFTWARE\Policies\Microsoft\Internet Explorer\IEDevTools",
            r"SOFTWARE\Policies\Microsoft\Internet Explorer\Restrictions"
        ]

        for ie_path in ie_registry_paths_current_user:
            # 레지스트리 키 추가
            ie_registry_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, ie_path)
            winreg.SetValueEx(ie_registry_key, "Disabled", 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(ie_registry_key)
        
        print("IE 모든 버전의 개발자 도구 방지 레지스트리 키가 성공적으로 추가되었습니다.")
    
    except PermissionError:
        print("관리자 권한으로 실행해주세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

def disable_edge_dev():
    try:
        # HKEY_LOCAL_MACHINE 경로 설정
        edge_registry_path = r"SOFTWARE\Policies\Microsoft\Edge"
        
        edge_registry_key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, edge_registry_path)
        winreg.SetValueEx(edge_registry_key, "DeveloperToolsAvailability", 0, winreg.REG_DWORD, 2)
        winreg.CloseKey(edge_registry_key)
        
        print("Edge 개발자 도구 방지 레지스트리 키가 성공적으로 추가되었습니다.")
    
    except PermissionError:
        print("관리자 권한으로 실행해주세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

def disable_chrome_dev():
    try:
        # HKEY_LOCAL_MACHINE 하위 경로 설정
        chrome_registry_path = r"SOFTWARE\Policies\Google\Chrome"
        
        chrome_registry_key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, chrome_registry_path)
        winreg.SetValueEx(chrome_registry_key, "DeveloperToolsDisabled", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(chrome_registry_key)
        
        print("Chrome 개발자 도구 방지 레지스트리 키가 성공적으로 추가되었습니다.")
    
    except PermissionError:
        print("관리자 권한으로 실행해주세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

def disable_firefox_dev():
    try:
        # Firefox 설정 파일 경로
        firefox_profiles_path = os.path.join(os.environ['APPDATA'], r'Mozilla\Firefox\Profiles')
        for firefox_profile in os.listdir(firefox_profiles_path):
            firefox_prefs_file = os.path.join(firefox_profiles_path, firefox_profile, 'prefs.js')
            if os.path.exists(firefox_prefs_file):
                with open(firefox_prefs_file, 'a') as firefox_file:
                    firefox_file.write('\nuser_pref("devtools.policy.disabled", true);')
        
        print("Firefox 개발자 도구가 성공적으로 비활성화되었습니다.")
    
    except Exception as e:
        print(f"오류 발생: {e}")
def restart_explorer():
    try:
        # Windows Explorer를 재시작하여 변경 사항 적용
        subprocess.run(["taskkill", "/F", "/IM", "explorer.exe"])
        subprocess.run(["start", "explorer.exe"], shell=True)
        print("Windows Explorer가 재시작되었습니다.")
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    if ctypes.windll.shell32.IsUserAnAdmin():
        disable_ie_dev()
        disable_edge_dev()
        disable_chrome_dev()
        disable_firefox_dev()
        restart_explorer()
        print("적용되기 위해서는 컴퓨터의 재부팅이 필요합니다!")
    else:
        print("관리자 권한이 필요합니다.")
