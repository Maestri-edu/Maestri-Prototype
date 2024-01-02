import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { StatusBar } from "react-native";

import Home from "./src/pages/home";
import Login from "./src/pages/SingIn";
import SignUp from "./src/pages/SignUp";

const Stack = createNativeStackNavigator();

const CustomHeader = ({ title }) => {
  return (
    <View style={{ flexDirection: 'row', justifyContent: 'center', alignItems: 'center' }}>
      {/* Adicione seus componentes personalizados do cabeçalho aqui */}
      <Text style={{ fontSize: 18, fontWeight: 'bold' }}>{title}</Text>
    </View>
  );
};

const app = () => {
  return (
    <NavigationContainer>
      <StatusBar translucent backgroundColor="transparent"/>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen
          name="Home"
          component={Home}
          options={{ headerShown: false,statusBarTranslucent:true }}
        />
        <Stack.Screen
          name="SignIn"
          component={Login}
          options={{ headerShown: false,statusBarTranslucent:true }}
        />
        <Stack.Screen
          name="SignUp"
          component={SignUp}
          options={{ headerShown: false,statusBarTranslucent:true }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
};

export default app;
