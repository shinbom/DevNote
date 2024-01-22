# 사이드 채널 공격 대책

## Site Isolation

컴퓨터의 CPU등 하드웨어에 대한 공격을 `사이드 채널 공격(side channel attack)`이라고 한다.

### Spectre(스펙터)

2018발생

CPU의 아키텍처의 취약성을 악용한 공격 방법.

접근 불가능한 메모리 안의 데이터에 대해 추측이 가능한 것이 입증됨.

---

프로세스 분리는 출처 단위로 이루어지며, 이 구조를 `Site Isolation`이라고 한다.

Site Isolation의 사이트는 출처와 다른 정의를 가지는 `보안의 경계`이다.

Site Isolation이 생기기 전에는 Iframe에 삽입된 다른 사이트의 접근을 막을 방법이 없었으나, Site Isolation에 의해 다른 사이트의 메모리 데이터에 접근하는 것을 막을 수 있다.

---

## Cross-Origin Isolation

Site Isolation을 통해 대부분의 사이드 채널 공격을 막을 수느는 있지만, 출처 단위의 사이드 채널 공격은 막지 못한다.

Spectre에 사용된 `SharedArrayBuffer`에 의해 브라우저의 API가 무효화 되기도 했다.

이에 대한 대비책으로, 출처마다 프로세스를 나누어 사이드 채널 공격이 발생하지 않는 것을 보장할 수 있어야 한다.

이처럼 프로세스를 분리하는 구조를 `Cross-Origin Isolation`이라고 한다.

`Cross-Origin Isolation`를 활성화 하는 방법은 다음과 같다.

- CORP(cross-origin resource policy)
- COEP(cross-origin embedder policy)
- COOP(cross-origin openner policy)
