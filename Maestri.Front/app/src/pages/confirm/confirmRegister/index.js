import { TouchableOpacity, View,Text } from "react-native"
import stylesComponent from "../../../design-System/components-styles"
import BackGround from "../../../components/backgroud"
import Title from "../../../components/title"
import { useNavigation } from "@react-navigation/native"


const ConfirmRegister = () => {
    const navigation = useNavigation();

    const goBack = ()=>{
        navigation.navigate("Home")
    }

    return(
        <View style={stylesComponent.container}>
            <BackGround/>
            <View style={stylesComponent.contentBox}>
                <Title title={"Confirmar registro"}/>
                <Text style={stylesComponent.text}> Enviamos uma menssagem de confirmação no seu WhatsApp, por favor verificar !</Text>
                <TouchableOpacity onPress={goBack} style={stylesComponent.button}>
                    <Text style={stylesComponent.buttonText}> voltar </Text>
                </TouchableOpacity>
            </View>
        </View>
    )
}

export default ConfirmRegister