import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  version = 'undetermined'
  ngOnInit(): void {
    fetch(this.getBackendUrl() + '/version', {
      method: 'GET',
      headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
      }
  })
     .then(response => {console.log(response); return response.json()})
     .then(response => {
      this.version = response['version'];
      console.log(JSON.stringify(response))})
  }



  faktor = new FormControl('')


setOperation(arg0: string) {
  this.operation = arg0;
}

value ="0"
operation = ''
getOperation() {
  return this.operation;
}
getCurrentValue() {
  return this.value;
}

addToFaktor(arg0: string) {
  this.faktor.setValue(this.faktor.getRawValue()+arg0);

}
getBackendUrl(){
  if (location.href.includes('localhost')){
    console.log('localhost')
    return 'http://localhost:8100'
  }

  if (location.href.includes('3.72.104.151:85')){
    console.log('prod')
    return 'http://3.72.104.151:86'
  }
  console.log('dev')
  return  'http://3.72.104.151:10086'

}



queryBackend(){
  if(this.operation == "+"){
    fetch(this.getBackendUrl() + '/add', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ "wert1": this.value, "wert2": this.faktor.getRawValue() })
})
   .then(response => response.json())
   .then(response => {
    this.value = response;
    this.faktor.setValue('')
    console.log(JSON.stringify(response))})
  }
  if(this.operation == "*"){

    fetch(this.getBackendUrl() + '/mul', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ "wert1": this.value, "wert2": this.faktor.getRawValue() })
})
   .then(response => response.json())
   .then(response => {
    this.value = response;
    this.faktor.setValue('')
    console.log(JSON.stringify(response))})
  }
  if(this.operation == "-"){
    fetch(this.getBackendUrl() + '/sub', {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({ "wert1": this.value, "wert2": this.faktor.getRawValue() })
})
   .then(response => response.json())
   .then(response => {
    this.value = response;
    this.faktor.setValue('')
    console.log(JSON.stringify(response))})
  }
}

  title = 'frontendus';

}


