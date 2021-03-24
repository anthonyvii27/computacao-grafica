void setup() {
  size(800, 600);
}

void draw() {
  background(#F4E3B2);
  
  float p1x = 100;
  float p1y = 500;
  float p2x = mouseX;
  float p2y = mouseY;
  float p3x = 700;
  float p3y = 100;
  
  beginShape();
  
  vertex(p1x, p1y);
  for(float t = 0; t <= 1; t += 0.05) {
    float ax = p1x + t * (p2x - p1x);
    float bx = p2x + t * (p3x - p2x);
    float cx = ax + t * (bx - ax);
    float ay = p1y + t * (p2y - p1y);
    float by = p2y + t * (p3y - p2y);
    float cy = ay + t * (by - ay);
    vertex(cx,cy);  
  }
  
  vertex(p3x, p3y);
  stroke(#EFC88B);
  strokeWeight(3);
  strokeJoin(ROUND);
  fill(#FE5F55);
  endShape(CLOSE);
}
