import { Text, View } from "react-native"
import { NavigationContainer } from "@react-navigation/native";
import { createBottomTabNavigator } from "@react-navigation/bottom-tabs";
import { StatusBar } from "react-native";
import Icon from "react-native-vector-icons/MaterialIcons";

import HomeResources from "./homeResources";
import IconMaestriTab from "./homeResources/IconMaestriTab";

const Tab = createBottomTabNavigator();

const Resources = () => {
    return (
        <NavigationContainer independent={true}>
            <StatusBar translucent backgroundColor="transparent" barStyle={"dark-content"} />
            <Tab.Navigator>
                <Tab.Screen
                    name="HomeResources"
                    component={HomeResources}
                    options={{
                        headerShown: false,
                        statusBarTranslucent: true,
                        tabBarIcon: ({ color, size }) => (
                            <Icon name={"home"} size={24} />
                        ),
                        tabBarLabel: "home",
                        tabBarLabelStyle: { color: "black" }
                    }}
                />
                <Tab.Screen
                    name="add"
                    component={HomeResources}
                    options={{
                        headerShown: false,
                        statusBarTranslucent: true,
                        tabBarIcon: ({ color, size }) => (
                            <Icon name={"add"} size={24} />
                        ),
                        tabBarLabel: "cadastrar",
                        tabBarLabelStyle: { color: "black" }
                    }}
                />
                <Tab.Screen
                    name="home"
                    component={HomeResources}
                    options={{
                        headerShown: false,
                        statusBarTranslucent: true,
                        tabBarIcon: ({ color, size }) => (
                            <IconMaestriTab />
                        ),
                        tabBarLabel: "",

                    }}
                />
                <Tab.Screen
                    name="students"
                    component={HomeResources}
                    options={{
                        headerShown: false,
                        statusBarTranslucent: true,
                        tabBarIcon: ({ color, size }) => (
                            <Icon name={"person"} size={24} />
                        ),
                        tabBarLabel: "ver alunos",
                        tabBarLabelStyle: { color: "black" }
                    }}
                />
                <Tab.Screen
                    name="attachMoney"
                    component={HomeResources}
                    options={{
                        headerShown: false,
                        statusBarTranslucent: true,
                        tabBarIcon: ({ color, size }) => (
                            <Icon name={"attach-money"} size={24} />
                        ),
                        tabBarLabel: "pagar",
                        tabBarLabelStyle: { color: "black" }
                    }}
                />
            </Tab.Navigator>
        </NavigationContainer>
    )
}

export default Resources