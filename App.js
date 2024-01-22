import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { StatusBar } from "react-native";

import Home from "./app/src/pages/home"
import Login from "./app/src/pages/SingIn";
import Resources from "./app/src/pages/resources";
import Register from "./app/src/pages/register";
import ConfirmRegister from "./app/src/pages/confirm/confirmRegister";
import NotConfirmRegister from "./app/src/pages/confirm/notConfirmRegister";
import ComplementaryRegisterI from "./app/src/pages/complementaryRegister/complementaryRegister-I.js";
import ComplementaryRegisterII from "./app/src/pages/complementaryRegister/complementaryRegister-II.js";
// import ComplementaryRegisterIII from "./app/src/pages/complementaryRegister/complementaryRegister-III.js";

const Stack = createNativeStackNavigator();

const app = () => {
  return (
    <NavigationContainer>
      <StatusBar translucent backgroundColor="transparent" />
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen
          name="Home"
          component={Home}
          options={{ headerShown: false, statusBarTranslucent: true }}
        />
        <Stack.Screen
          name="SignIn"
          component={Login}
          options={{ headerShown: false, statusBarTranslucent: true }}
        />
        <Stack.Screen
          name="Register"
          component={Register}
          options={{ headerShown: false, statusBarTranslucent: true }}
        />
        <Stack.Screen
          name="Resources"
          component={Resources}
          options={{ headerShown: false, statusBarTranslucent: true }}
        />
        <Stack.Screen
          name="ComplementaryRegister/personData"
          component={ComplementaryRegisterI}
          options={{ headerShown: false, statusBarTranslucent: true }}
        />
        <Stack.Screen
          name="ComplementaryRegister/PersonLocation"
          component={ComplementaryRegisterII}
          options={{ headerShown: false, statusBarTranslucent: true }}
        />
        {/* <Stack.Screen
          name="ComplementaryRegister/teste"
          component={ComplementaryRegisterIII}
          options={{ headerShown: false, statusBarTranslucent: true }}
        /> */}
        <Stack.Screen
          name="ConfirmRegister"
          component={ConfirmRegister}
          options={{ headerShown: false, statusBarTranslucent: true }}
        />
        <Stack.Screen
          name="NotConfirmRegister"
          component={NotConfirmRegister}
          options={{ headerShown: false, statusBarTranslucent: true }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default app;