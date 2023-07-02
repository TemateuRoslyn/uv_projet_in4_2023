import { Component } from '@angular/core';
// import { SettingDTO } from 'src/app/generated';
import { NavigationService } from 'src/app/services/navigation.service';

@Component({
  selector: 'app-default-footer',
  templateUrl: './default-footer.component.html',
  styleUrls: ['./default-footer.component.css'],
})
export class DefaultFooterComponent {

  public setting?: any; // SettingDTO;

  public constructor(
    public navService: NavigationService,
    ) {
    this._initialisation();
  }

  public _initialisation() {
  }

}