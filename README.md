# DELDEVTOOL
군 시절에 만들었던 크롬, 엣지, 인터넷 익스플로러, FIREFOX 개발자 도구 방지 프로그램입니다.

DELDEVTOOL에 있는 disable.py는 크롬, 엣지, 인터넷익스플로러 FIREFOX를 개발자 도구를 막는 소스코드입니다. 해당 코드를 실행하기 위해서는 관리자권한으로 실행을 하여야 합니다.

또한 enable.py는 다시 개발자 도구를 사용할 수 있게 disable.py로 추가되었던 레지스트리키를 삭제합니다. 이 코드 또한 관리자 권한으로 실행을 해야 합니다.

dist에 있는 exe 파일은 
pyinstaller --onefile --noconsole disable.py로 만들어진 실행파일입니다. 실행하기 위해 관리자 권한으로 실행을 하여야 합니다.
