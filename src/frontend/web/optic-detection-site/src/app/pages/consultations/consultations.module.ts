import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ConsultationsRoutingModule } from './consultations-routing.module';
import { ConsultationsComponent } from './components/consultations/consultations.component';


@NgModule({
  declarations: [ConsultationsComponent],
  imports: [
    CommonModule,
    ConsultationsRoutingModule
  ]
})
export class ConsultationsModule { }
