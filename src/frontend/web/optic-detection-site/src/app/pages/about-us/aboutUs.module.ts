import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';


import { AboutURoutingModule } from './aboutUs-routing.module';
import { AboutUsComponent } from './components/about-us/about-us.component';

@NgModule({
  declarations: [ AboutUsComponent],
  imports: [
    CommonModule,
    AboutURoutingModule,
  ],
  providers: [],
  exports: []
})
export class AboutUsModule {}
