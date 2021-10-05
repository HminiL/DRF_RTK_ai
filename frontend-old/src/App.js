import { BackTracking, BruteForce, DivideConquer, DynamicProgramming, Greedy } from "algorithm";
import { Counter, Home, Navigation, Todo, SignUp } from "common";
import { Linear, Mathmatics, Nonlinear } from "datastructure";
import React from "react";
import { Route, Switch, Redirect } from 'react-router-dom';
import { createStore, combineReducers } from 'redux'
import { Provider } from 'react-redux'
import { todoReducer, userReducer } from 'reducers'
const rootReducer = combineReducers({todoReducer, userReducer })
const store = createStore(rootReducer)

const App = () => (
  <Provider store = {store}>
    <Navigation />
    <Switch>
      <Route  exact path= '/' component = {Home}/>
      <Redirect  from = '/home' to = {'/'}/>
      <Route  exact path= '/counter' component = {Counter}/>
      <Route  exact path= '/sign-up' component = {SignUp}/>
      <Route  exact path= '/todo' component = {Todo}/>
      <Route  exact path= '/math' component = {Mathmatics}/>  
      <Route  exact path= '/linear' component = {Linear}/>  
      <Route  exact path= '/nonlinear' component = {Nonlinear}/>  
      <Route  exact path= '/brute-force' component = {BruteForce}/>  
      <Route  exact path= '/divide-conquer' component = {DivideConquer}/>  
      <Route  exact path= '/greedy' component = {Greedy}/>  
      <Route  exact path= '/dp' component = {DynamicProgramming}/>  
      <Route  exact path= '/back-tracking' component = {BackTracking}/>  
    </Switch>
  </Provider>
)

export default App