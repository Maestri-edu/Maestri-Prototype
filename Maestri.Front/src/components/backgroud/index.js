import React from "react";
import { View, ImageBackground } from "react-native";
import imageBackground from "../../../assets/backgroundImage.jpg";
import { LinearGradient } from "expo-linear-gradient";
import stylesComponent from "../../design-System/components-styles";
import styles from "./styles";

const BackGround = () => {
  return (
    <View style={stylesComponent.container}>
      <ImageBackground
        source={imageBackground}
        style={styles.image}
      >
        <View style={styles.mask} />
        <LinearGradient
          colors={['#000090', "transparent"]}
          style={styles.gradient}
        />
      </ImageBackground>
    </View>
  );
};

export default BackGround;
