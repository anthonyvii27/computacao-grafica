void setup() {
  size(450, 450);
}

void draw(){
  background(#F4E3B2);
  
  int points = 10; // Star points
  
  int externalRadiusLimiter = 100;
  float externalRadius = round(map(mouseX, 0, width + 100, externalRadiusLimiter, height - 200));
  
  int innerRadius = 80;
  float move = TWO_PI/points;

  translate(width/2, height/2);
  rotate(PI/10);
  
  float x = 0;
  float y = 0;
  
  beginShape(); 
    for(int i=0; i <= points; i++) {
      if(i % 2 != 0) {
        x = externalRadius * cos(move * i)/2;
        y = externalRadius * sin(move * i)/2;     
        vertex(x,y);
      } else {
        x = innerRadius * cos(move * i)/2;
        y = innerRadius * sin(move * i)/2; 
        vertex(x,y);
      }
    }
  endShape();
    
  stroke(#EFC88B);
  strokeWeight(3);
  strokeJoin(ROUND);
  fill(#FE5F55);
}