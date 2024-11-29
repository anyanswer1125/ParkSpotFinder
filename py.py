import cv2
import numpy as np

def test_with_image(image_path):
    print("이미지 로딩 중...")
    # 이미지 읽기
    image = cv2.imread(image_path)
    
    if image is None:
        print("이미지를 불러올 수 없습니다!")
        return
    
    # 이미지 크기가 너무 큰 경우 리사이즈
    height, width = image.shape[:2]
    if width > 1200:
        scaling_factor = 1200 / width
        image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor)
    
    # 원본 이미지 표시
    cv2.imshow('Original Image', image)
    
    # 이미지 처리
    # 그레이스케일 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 노이즈 제거를 위한 블러 처리
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Canny 엣지 검출
    edges = cv2.Canny(blurred, 50, 150)
    
    # 처리된 이미지 표시
    cv2.imshow('Processed Image', edges)
    
    print("아무 키나 누르면 종료됩니다.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 이미지 경로 지정
    image_path = 'test_image.jpg'  # 여기에 테스트하고 싶은 이미지 경로를 넣으세요
    test_with_image(image_path)