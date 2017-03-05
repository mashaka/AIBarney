//
//  CategoryGridController.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 05/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import UIKit
import Hero

class CategoryGridController: UIViewController, UICollectionViewDelegate, UICollectionViewDataSource, UICollectionViewDelegateFlowLayout {
    
    @IBOutlet weak var collectionView: UICollectionView!
    
    var categories: [Category]?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        collectionView.heroModifiers = [.cascade]
    }
    
    func numberOfSections(in collectionView: UICollectionView) -> Int {
        return 1
    }
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return categories == nil ? 0 : categories!.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "categoryCell", for: indexPath)
        
        return cell
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        let size = (UIScreen.main.bounds.width - 50.0) / 2
        return CGSize(width: size, height: size)
    }
}
