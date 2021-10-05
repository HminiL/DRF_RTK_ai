import { configureStore } from '@reduxjs/toolkit';
import counterReducer from 'features/counter/modules/counterSlice';
import todoReducer from 'features/todos/modules/todoSlice';
import commonReducer from 'common/modules/commonSlice'

export const store = configureStore({
  reducer: {
    counter: counterReducer,
    common : commonReducer,
    todos : todoReducer,
  },
});
