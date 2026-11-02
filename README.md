# server-monitor

🩺 Rocky Linux 서버 상태를 한 번에 점검하는 스크립트

## 기능
- 호스트 이름, IP, 현재 시간, 가동 시간 출력
- 디스크, 메모리, CPU 사용량 출력
- 접속 중인 사용자 확인
- 디스크 사용량 80% 이상 시 경고

## 실행 방법
```bash
chmod +x monitor.sh
./monitor.sh
```

결과를 파일로 저장하려면 다음과 같이 실행합니다.
```bash
mkdir -p logs
./monitor.sh > logs/$(date +%Y%m%d_%H%M).log
```

## 실행 환경
- Rocky Linux (VMware VM)
- MobaXterm으로 SSH 접속해 작업

## 로드맵
- [x] 1단계: 쉘 스크립트로 서버 상태 출력
- [ ] 2단계: Python으로 재작성, 설정은 YAML로 분리
- [ ] 3단계: SSH로 여러 VM 상태 수집
- [ ] 4단계: 수집 결과 DB 저장

## 배운 점
- (cat > 파일명 << 'EOF'~EOF -> vi를 열지 않고도 파일로 저장하는 방법, '>'와 '>>'의 차이)
