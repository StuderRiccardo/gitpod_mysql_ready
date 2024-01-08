import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { Root } from './info';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  //@ts-ignore
  data: Root = []
  constructor(private http: HttpClient) {
  }
  //SINK WHILE YOU BREATHE IN HALLUCINATION, ACCEPT THIS DESCENT INTO THE NIGHT,
  //RELEASING YOUR GRASP TO, INDUCE SEPARATION PLUNGED INTO THE SHADOWS, LOT IN 
  //SENSATION WERE FREE FALLING DOWN INTO THE EVERBLACK, CAN YOU FEEL IT? THESE PINS AND NEEDLES
  req(funy: string) {
    
    this.http.get<Root>("https://5000-colombettiriccar-flask-uqpzm5hjejh.ws-eu107.gitpod.io/" + funy).subscribe(e => {
      this.data = e;
    });
  }
}