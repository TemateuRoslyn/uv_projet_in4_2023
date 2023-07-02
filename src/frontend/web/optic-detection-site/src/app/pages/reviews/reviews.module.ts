import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';


import { ReviewsRoutingModule } from './reviews-routing.module';
import { ReviewsComponent } from './components/reviews/reviews.component';

@NgModule({
  declarations: [ ReviewsComponent],
  imports: [
    CommonModule,
    ReviewsRoutingModule,
  ],
  providers: [],
  exports: []
})
export class ReviewsModule {}
