#version 330 core

layout(location = 0) out vec4 fragColor;

in vec3 normal;
in vec3 fragPos;

uniform vec3 color;



void main(){
    vec3 fcolor;
    if (length(color) > 0){
        float north = fragPos.y+0.5;
        float south = 1.0-north;
        fcolor = vec3(south*0.5,0,north*0.5);
    }
    else{
        fcolor = color;
    }
    
    fragColor = vec4(fcolor, 1.0);
}