import winreg
import os
import subprocess
import ctypes

def enable_ie_devtools():
    try:
        # HKEY_LOCAL_MACHINE 경로 설정
        ie_registry_paths = [
            r"SOFTWARE\Policies\Microsoft\Internet Explorer\IEDevTools",
            r"SOFTWARE\WOW6432Node\Policies\Microsoft\Internet Explorer\IEDevTools",
            r"SOFTWARE\Policies\Microsoft\Internet Explorer\Restrictions",
            r"SOFTWARE\WOW6432Node\Policies\Microsoft\Internet Explorer\Restrictions"
        ]

        for ie_path in ie_registry_paths:
            try:
                winreg.DeleteKey(winreg.HKEY_LOCAL_MACHINE, ie_path)
            except FileNotFoundError:
                pass

        # HKEY_CURRENT_USER 경로 설정
        ie_registry_paths_current_user = [
            r"SOFTWARE\Policies\Microsoft\Internet Explorer\IEDevTools",
            r"SOFTWARE\Policies\Microsoft\Internet Explorer\Restrictions"
        ]

        for ie_path in ie_registry_paths_current_user:
            try:
                # 레지스트리 키 삭제
                winreg.DeleteKey(winreg.HKEY_CURRENT_USER, ie_path)
            except FileNotFoundError:
                pass

        print("IE 모든 버전의 개발자 도구 방지 레지스트리 키가 성공적으로 삭제되었습니다.")
    
    except PermissionError:
        print("관리자 권한으로 실행해주세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

def enable_edge_dev():
    try:
        # HKEY_LOCAL_MACHINE 경로 설정
        edge_registry_path = r"SOFTWARE\Policies\Microsoft\Edge"
        #레지스트리 키 삭제
        edge_registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, edge_registry_path, 0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(edge_registry_key, "DeveloperToolsAvailability")
        winreg.CloseKey(edge_registry_key)
        
        print("Edge 개발자 도구 방지 레지스트리 키가 성공적으로 삭제되었습니다.")
    
    except FileNotFoundError:
        print("해당 방지 레지스트리 키가 존재하지 않습니다.")
    except PermissionError:
        print("관리자 권한으로 실행해주세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

def enable_chrome_dev():
    try:
        # HKEY_LOCAL_MACHINE 경로 설정
        chrome_registry_path = r"SOFTWARE\Policies\Google\Chrome"
        # 레지스트리 키 삭제 
        chrome_registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, chrome_registry_path, 0, winreg.KEY_SET_VALUE)
        winreg.DeleteValue(chrome_registry_key, "DeveloperToolsDisabled")
        winreg.CloseKey(chrome_registry_key)
        
        print("Chrome 개발자 도구 방지 레지스트리 키가 성공적으로 삭제되었습니다.")
    
    except FileNotFoundError:
        print("해당  방지 레지스트리 키가 존재하지 않습니다.")
    except PermissionError:
        print("관리자 권한으로 실행해주세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

def enable_firefox_dev():
    try:
        # Firefox 설정 파일 경로
        firefox_profiles_path = os.path.join(os.environ['APPDATA'], r'Mozilla\Firefox\Profiles')
        for firefox_profile in os.listdir(firefox_profiles_path):
            firefox_prefs_file = os.path.join(firefox_profiles_path, firefox_profile, 'prefs.js')
            if os.path.exists(firefox_prefs_file):
                with open(firefox_prefs_file, 'r') as file:
                    lines = file.readlines()
                with open(firefox_prefs_file, 'w') as file:
                    for line in lines:
                        if 'user_pref("devtools.policy.disabled", true);' not in line:
                            file.write(line)
        
        print("Firefox 개발자 도구가 성공적으로 활성화되었습니다.")
    
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
    # 관리자 권한 확인
    if ctypes.windll.shell32.IsUserAnAdmin():
        enable_ie_devtools()
        enable_edge_devtools()
        enable_chrome_devtools()
        enable_firefox_devtools()
        restart_explorer()
    else:
        print("이 스크립트를 실행하려면 관리자 권한이 필요합니다.")
