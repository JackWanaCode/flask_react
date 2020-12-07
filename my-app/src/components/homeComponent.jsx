import React, {Component} from 'react';
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import HeaderComponent from './headerComponent';
import LoginComponent from './loginComponent';
import WelcomeComponent from './welcomeComponent';
import LogoutComponent from './logoutComponent';
import RegisterComponent from './registerComponent';


class HomeComponent extends Component {


    render() {
        return (
            <div>
                <Router>
                    <HeaderComponent/>
                    <Switch>
                        <Route path="/" exact component={WelcomeComponent}/>
                        <Route path="/login" exact component={LoginComponent}/>
                        <Route path='/logout' exact component={LogoutComponent}/>
                        <Route path='/register' exact component={RegisterComponent}/>
                        <Route component={ErrorComponent}/>
                    </Switch>
                </Router>
            </div>
        )
    }
}

function ErrorComponent() {
    return <div>An Error Occured</div>
}

export default HomeComponent;