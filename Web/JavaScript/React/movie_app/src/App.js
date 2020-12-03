import React from 'react';
import { HashRouter, Route } from "react-router-dom"
import About from "./routes/About"
import Home from "./routes/Home"
import Navi from "./components/Navigator"

function App() {
    return <HashRouter>
        <Navi/>
        <Route path="/" exact={true} component={Home}/>
        <Route path="/about" component={About}/>
    </HashRouter>
}

export default App;