import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';


import { BooksRoutingModule } from './books-routing.module';
import { BooksComponent } from './components/books/books.component';

@NgModule({
  declarations: [ BooksComponent],
  imports: [
    CommonModule,
    BooksRoutingModule,
  ],
  providers: [],
  exports: []
})
export class BooksModule {}
