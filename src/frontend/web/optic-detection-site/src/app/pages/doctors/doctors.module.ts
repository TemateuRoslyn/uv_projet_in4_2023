import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';


import { DoctorsComponent } from './components/doctors/doctors.component';
import { DoctorsRoutingModule } from './doctors-routing.module';

@NgModule({
  declarations: [ DoctorsComponent],
  imports: [
    CommonModule,
    DoctorsRoutingModule,
  ],
  providers: [],
  exports: []
})
export class DoctorsModule {}
