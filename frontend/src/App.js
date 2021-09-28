import { BackTracking, BruteForce, DivideConquer, DynamicProgramming, Greedy } from "algorithm";
import { Counter, Home, Navigation, Todo } from "common";
import { Linear, Mathmatics, Nonlinear } from "datastructure";
import React from "react";
import { Route, Switch, Redirect } from 'react-router-dom';
import { createStore, combineReducers } from 'redux'
import { Provider } from 'react-redux'
import { todoReducer } from 'reducers'
const rootReducer = combineReducers({todoReducer})
const store = createStore(rootReducer)

const App = () => (
  <Provider store = {store}>
    <Navigation />
    <Switch>
      <Route  exact path= '/' component = {Home}/>
      <Redirect  from = '/home' to = {'/'}/>
      <Route  exact path= '/counter' component = {Counter}/>
      <Route  exact path= '/todo' component = {Todo}/>
      <Route  exact path= '/math' component = {Mathmatics}/>  
      <Route  exact path= '/linear' component = {Linear}/>  
      <Route  exact path= '/nonlinear' component = {Nonlinear}/>  
      <Route  exact path= '/bruteForce' component = {BruteForce}/>  
      <Route  exact path= '/divideConquer' component = {DivideConquer}/>  
      <Route  exact path= '/greedy' component = {Greedy}/>  
      <Route  exact path= '/dynamicP' component = {DynamicProgramming}/>  
      <Route  exact path= '/backTracking' component = {BackTracking}/>  
    </Switch>
  </Provider>
)

export default App