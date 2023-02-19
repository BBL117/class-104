import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img, "Mercury", (85, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (155, 155, 155), 2)
cv2.putText(img, "Venus", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (155, 155, 155), 2)
cv2.putText(img, "Earth", (330, 250), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (155, 155, 155), 2)
cv2.putText(img, "Mars", (405, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (155, 155, 155), 2)
cv2.putText(img, "Jupiter", (550, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (155, 155, 155), 2)
cv2.putText(img, "Saturn", (750, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (155, 155, 155), 2)
cv2.putText(img, "Uranus", (950, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (155, 155, 155), 2)
cv2.putText(img, "Neptune", (1125, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (155, 155, 155), 2)


cv2.imshow("output", img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg", img)
