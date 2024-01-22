import { View,Text, StatusBar } from "react-native"

import stylesComponent from "../../../design-System/components-styles"
import Information from "./information"
import Actions from "./actions/"
import CarouselResources from "./carousel"

const HomeResources = () => {
    return (
        <View style={{ ...stylesComponent.container}}>
            <StatusBar barStyle={"dark-content"}/>
            <Information />
            <Actions/>
            <CarouselResources/>
        </View>
    )
}

export default HomeResources