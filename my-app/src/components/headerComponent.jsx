import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import {withRouter} from 'react-router';


class HeaderComponent extends Component {


    render () {
        return (
            <header>
                <nav>
                    <ul>
                        <li><Link to="/">Home</Link></li>
                        <li><Link to="/login">Login</Link></li>
                        <li><Link to="/logout">Logout</Link></li>
                        <li><Link to="/Register">Register</Link></li>
                    </ul>
                </nav>
            </header>
        )
    }
}

export default withRouter(HeaderComponent);