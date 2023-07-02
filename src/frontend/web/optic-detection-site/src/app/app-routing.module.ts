import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DefaultLayoutComponent } from './containers';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'home',
    pathMatch: 'full',
  },
  {
    path: '',
    component: DefaultLayoutComponent,
    data: {
      title: 'Home',
    },

    children: [
      {
        path: 'home',
        loadChildren: () =>
          import('./pages/home/home.module').then((m) => m.HomeModule),
      },
      {
        path: 'services',
        loadChildren: () =>
          import('./pages/services/services.module').then(
            (m) => m.ServicesModule
          ),
      },
      {
        path: 'consultation',
        loadChildren: () =>
          import('./pages/consultations/consultations.module').then(
            (m) => m.ConsultationsModule
          ),
      },
      {
        path: 'about-us',
        loadChildren: () =>
          import('./pages/about-us/aboutUs.module').then(
            (m) => m.AboutUsModule
          ),
      },
      {
        path: 'doctors',
        loadChildren: () =>
          import('./pages/doctors/doctors.module').then(
            (m) => m.DoctorsModule
          ),
      },
      {
        path: 'book',
        loadChildren: () =>
          import('./pages/books/books.module').then(
            (m) => m.BooksModule
          ),
      },
      {
        path: 'review',
        loadChildren: () =>
          import('./pages/reviews/reviews.module').then(
            (m) => m.ReviewsModule
          ),
      },
      {
        path: 'blogs',
        loadChildren: () =>
          import('./pages/blogs/blogs.module').then(
            (m) => m.BlogsModule
          ),
      }
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule { }
