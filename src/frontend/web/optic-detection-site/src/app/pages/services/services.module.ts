import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ServiceRoutingModule } from './services-routing.module';

import { ServicesComponent } from './components/services/services.component';

@NgModule({
  declarations: [ ServicesComponent],
  imports: [
    CommonModule,
    ServiceRoutingModule,
  ],
  providers: [],
  exports: []
})
export class ServicesModule {}
