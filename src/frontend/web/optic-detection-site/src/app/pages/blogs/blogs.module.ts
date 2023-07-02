import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';


import { BlogsRoutingModule } from './blogs-routing.module';
import { BlogsComponent } from './components/blogs/blogs.component';

@NgModule({
  declarations: [ BlogsComponent],
  imports: [
    CommonModule,
    BlogsRoutingModule,
  ],
  providers: [],
  exports: []
})
export class BlogsModule {}
