import winreg
import os

def disable_ie_devtools():
    try:
        # HKEY_LOCAL_MACHINE 하위 경로 설정
        ie_registry_paths = [
            r"SOFTWARE\Policies\Microsoft\Internet Explorer\IEDevTools",
            r"SOFTWARE\WOW6432Node\Policies\Microsoft\Internet Explorer\IEDevTools",
            r"SOFTWARE\Policies\Microsoft\Internet Explorer\Restrictions",
            r"SOFTWARE\WOW6432Node\Policies\Microsoft\Internet Explorer\Restrictions"
        ]

        for ie_path in ie_registry_paths:
            ie_registry_key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, ie_path)
            winreg.SetValueEx(ie_registry_key, "Disabled", 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(ie_registry_key)

        # HKEY_CURRENT_USER 하위 경로 설정
        ie_registry_paths_current_user = [
            r"SOFTWARE\Policies\Microsoft\Internet Explorer\IEDevTools",
            r"SOFTWARE\Policies\Microsoft\Internet Explorer\Restrictions"
        ]

        for ie_path in ie_registry_paths_current_user:
            ie_registry_key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, ie_path)
            winreg.SetValueEx(ie_registry_key, "Disabled", 0, winreg.REG_DWORD, 1)
            winreg.CloseKey(ie_registry_key)
        
        print("IE 모든 버전의 개발자 도구 레지스트리 키가 성공적으로 추가되었습니다.")
    
    except PermissionError:
        print("관리자 권한으로 실행해주세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

def disable_edge_devtools():
    try:
        # HKEY_LOCAL_MACHINE 하위 경로 설정
        edge_registry_path = r"SOFTWARE\Policies\Microsoft\Edge"
        
        edge_registry_key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, edge_registry_path)
        winreg.SetValueEx(edge_registry_key, "DeveloperToolsAvailability", 0, winreg.REG_DWORD, 2)
        winreg.CloseKey(edge_registry_key)
        
        print("Edge 개발자 도구 레지스트리 키가 성공적으로 추가되었습니다.")
    
    except PermissionError:
        print("관리자 권한으로 실행해주세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

def disable_chrome_devtools():
    try:
        # HKEY_LOCAL_MACHINE 하위 경로 설정
        chrome_registry_path = r"SOFTWARE\Policies\Google\Chrome"
        
        chrome_registry_key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, chrome_registry_path)
        winreg.SetValueEx(chrome_registry_key, "DeveloperToolsDisabled", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(chrome_registry_key)
        
        print("Chrome 개발자 도구 레지스트리 키가 성공적으로 추가되었습니다.")
    
    except PermissionError:
        print("관리자 권한으로 실행해주세요.")
    except Exception as e:
        print(f"오류 발생: {e}")

def disable_firefox_devtools():
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

if __name__ == "__main__":
    disable_ie_devtools()
    disable_edge_devtools()
    disable_chrome_devtools()
    disable_firefox_devtools()
