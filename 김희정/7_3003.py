'''
BOJ_3003_킹, 퀀, 룩, 비숍, 나이트, 폰
나의 idea : input + 출력 = 원래값
'''
#킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개

king, queen, rook, bishop, knight, pawn = map(int,input().split())
print(1-king, 1-queen, 2-rook, 2-bishop,2-knight, 8-pawn)