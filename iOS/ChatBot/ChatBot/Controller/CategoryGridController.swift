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
    
    var chatId: String?
    var categories: [Category]?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        collectionView.contentInset = UIEdgeInsetsMake(79.0, 15.0, 0.0, 15.0)
        collectionView.heroModifiers = [.cascade]
    }
    
    func numberOfSections(in collectionView: UICollectionView) -> Int {
        return 1
    }
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return categories == nil ? 0 : categories!.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "categoryCell", for: indexPath) as! CategoryCollectionViewCell
        
        cell.category = categories![indexPath.row]
        UIHelper.createColoredShadowOnView(view: cell)
        
        cell.heroModifiers = [.fade, .scale(0.5)]
        cell.categoryCoverImageView.heroID = "\(cell.category!.categoryType.name())_image"
        cell.heroID = "\(cell.category!.categoryType.name())_container"
        cell.heroModifiers = [.cornerRadius(13.0)]
        
        return cell
    }
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        performSegue(withIdentifier: "toCategory", sender: indexPath)
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "toCategory" {
            let indexPath = sender as! IndexPath
            (segue.destination as! SingleCategoryController).category = categories![indexPath.row]
            (segue.destination as! SingleCategoryController).chatId = chatId
        }
    }
    
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        let size = (UIScreen.main.bounds.width - 50.0) / 2
        return CGSize(width: size, height: size)
    }
    
    @IBAction func onClose(_ sender: Any) {
        dismiss(animated: true, completion: nil)
    }
}
