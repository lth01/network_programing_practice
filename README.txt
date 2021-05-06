1. 외부 기기에서 접속을 하기 위해서는 포트포워딩이 필요합니다.(각 피어들 모두)
ㄴ각 공유기의 포트포워딩 설명에 따라서 서버의 경우외부ip:9999를 포워딩해주십시오
ㄴ피어들의 경우 외부 ip:10000~50000을 포워딩해주십시오(같은 기기일 경우 상관 x)
ㄴ다른 프로세스들과의 접근을 피하기 위하여 10000~50000대의 포트를 사용하시길 권합니다.(필수사항 X)

2.서버 ip,port는 고정되어있습니다. 만약 서버 ip를 변경해서 사용해야할 경우 Client.py self.NAP_SERVER=ip부분을 변경하여 주십시오

3.본 파일들은 twisted프레임워크를 사용하여 구현되었습니다. https://pypi.org/project/Twisted/ 을 참고하여 모듈을 다운로드 받아주십시오
사용해야할 라이브러리:twisted,socket,random


실행순서

python NAP_SERVER.py
이후

python Client.py ....(여러개가 가능합니다.)


명령어 설명
[peer]=[ip,port](띄어쓰면안됩니다)

-help:사용가능한 명령어를 하나씩 출력합니다.

-online_users:NAP_SERVER에 접속되어있는 기기의 ip,port를 반환해 줍니다.(peer)

-connect [ip] [port]: (ip,port)인 피어에게 연결을 진행합니다.

-disconnect [peer]:connect 된 피어와 연결을 해제합니다.

-talk [peer] [message]:connect 된 피어에게 메세지를 전달합니다.

-logoff:NAP_SERVER에게 logoff 사실을 알리고 프로그램을 종료합니다.

별도의 문자열 입력시 :메세지가 온게 있는지 확인합니다.