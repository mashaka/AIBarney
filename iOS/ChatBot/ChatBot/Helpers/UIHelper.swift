//
//  UIHelper.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 04/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit
import AlamofireImage

class UIHelper {
    
    // Singleton   -------------------
    
    static let shared: UIHelper = UIHelper()
    
    let imageDownloader = ImageDownloader()
    let imageCache = AutoPurgingImageCache()
    
    // Static Shit -------------------
    
    static let orangeColor = UIColor(red: 235.0/255.0, green: 64.0/255.0, blue: 44.0/255.0, alpha: 1.0)
    static let pinkColor = UIColor(red: 217.0/255.0, green: 6.0/255.0, blue: 71.0/255.0, alpha: 1.0)
    
    static let shadowColor = UIColor(red: 223.0/255.0, green: 27.0/255.0, blue: 61.0/255.0, alpha: 1.0)
    
    static let grayTextColor = UIColor(red: 54.0/255.0, green: 54.0/255.0, blue: 54.0/255.0, alpha: 1.0)
    
    static func createGradientOnView(view: UIView, cornerRadius: CGFloat = 0.0) {
        let gradient = CAGradientLayer()
        
        gradient.frame = view.bounds
        gradient.colors = [pinkColor.cgColor, orangeColor.cgColor]
        gradient.cornerRadius = cornerRadius
        gradient.masksToBounds = true
        gradient.name = "chatbot-gradient"
        
        let oldGradienLayerIndex = view.layer.sublayers?.index(where: { layer -> Bool in
            return layer.name == "chatbot-gradient"
        })
        
        if oldGradienLayerIndex != nil {
            view.layer.replaceSublayer(view.layer.sublayers![oldGradienLayerIndex!], with: gradient)
        } else {
            view.layer.insertSublayer(gradient, at: 0)
        }
    }
    
    static func createColoredShadowOnView(view: UIView) {
        view.layer.shadowColor = shadowColor.cgColor
        view.layer.shadowOffset = CGSize(width: 0, height: 20)
        view.layer.shadowOpacity = 0.3;
        view.layer.shadowRadius = 15.0;
    }
    
    // -------------------------------
    
    func navBarFont() -> UIFont {
        return UIFont(name: "Lato-Regular", size: 18.0)!
    }
    
    func barButtonFont() -> UIFont {
        return UIFont(name: "Lato-Semibold", size: 18.0)!
    }
    
    func setNavBarAppearance() {
        let navAppearance = UINavigationBar.appearance()
        navAppearance.tintColor = UIHelper.pinkColor
        navAppearance.titleTextAttributes = [NSForegroundColorAttributeName: UIHelper.grayTextColor,
            NSFontAttributeName: navBarFont()]
        
        UIBarButtonItem.appearance().setTitleTextAttributes([NSFontAttributeName : barButtonFont()], for: .normal)
    }
    
    // -------------------------------
    
    static func getMainStoruboard() -> UIStoryboard {
        return UIStoryboard(name: "Main", bundle: nil)
    }
    
    static func createAuthController() -> UIViewController {
        let auth: AuthController = UIHelper.getMainStoruboard().instantiateViewController(withIdentifier: "authController") as! AuthController
        
        auth.modalTransitionStyle = .flipHorizontal
        
        return auth
    }
    
    // -------------------------------
    
    func downloadAndSetImage(imageView: UIImageView, imageUrl: URL?) {
        func setImageAnimated(imageView: UIImageView, image: UIImage) {
            DispatchQueue.main.async {
                UIView.transition(with: imageView,
                                  duration: 0.2,
                                  options: .transitionCrossDissolve,
                                  animations: {
                                    imageView.image = image
                },
                                  completion: nil)
            }
        }
        
        guard let url = imageUrl else {
            //print("Bad Image Url")
            return
        }
        
        guard let imageInCache = imageCache.image(for: URLRequest(url: url)) else {
            imageDownloader.download(URLRequest(url: url)) { response in
                if let image = response.result.value {
                    self.imageCache.add(image, for: URLRequest(url: url))
                    setImageAnimated(imageView: imageView, image: image)
                }
            }
            return
        }
        
        setImageAnimated(imageView: imageView, image: imageInCache)
    }
}
