# 작업 노트

## 2026-11-09 Mindstream LAB 디자인시스템 적용

- 기준: claude.ai의 "Mindstream LAB" Design System 아티팩트(project/README.md, tokens.json, components/bundle.css).
- 기본 테마는 Night. 인쇄할 때만 Cream 값으로 바꾼다. 화면 테마 전환 버튼은 요청 범위 밖이라 넣지 않았다.
- 작사(분홍)/작곡(파랑) 모드별 강조색은 없앴다. 디자인시스템은 한 화면에 강조색 하나(accent)만 허용한다. 모드 구분은 키커 문구(LYRICS / COMPOSE)로 한다.
- 그라데이션은 워드마크에만 쓴다. 제목 글자·버튼·카드의 그라데이션을 모두 걷어냈다.
- 디자인시스템은 이모지를 쓰지 않는다고 하지만, 사용자가 이모지를 남기길 원해 원래 이모지를 모두 유지했다(수업 도구라 항목을 빨리 알아보는 데 도움). 경고에는 이모지 옆에 "주의" 낱말을 붙여 색에만 기대지 않게 했다.
- 카드에는 테두리·그림자를 쓰지 않는다. 대신 선택 상태는 accent 2px 안쪽 링과 체크 표시로 보여 준다(색만으로 구분하지 않기 위해).
- 선택 칩은 디자인시스템의 KeywordChip(파이프라인 색 칩)과 쓰임이 달라 버튼 규칙(accent 채움 + on-accent 글자)을 따랐다.
- JS 안의 인라인 style이 `--text`, `--sub`, `--muted`, `--warn`, `--lyric` 등을 쓰고 있어, 새 토큰을 가리키는 별칭 변수로 남겨 두었다.
- 크레딧 로고는 `../mindstream-ci/png`의 compact 로고를 `assets/`로 복사해 쓴다(Night는 -dark 파일).
