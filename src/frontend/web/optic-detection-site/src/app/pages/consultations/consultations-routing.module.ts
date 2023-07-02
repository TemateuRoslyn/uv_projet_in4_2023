import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ConsultationsComponent } from './components/consultations/consultations.component';

const routes: Routes = [
  {
    path: '',
    component: ConsultationsComponent,
    data: {
      title: "Consultations"
    }
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ConsultationsRoutingModule { }
