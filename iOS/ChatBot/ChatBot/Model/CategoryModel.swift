//
//  CategoryModel.swift
//  ChatBot
//
//  Created by Alexander Danilyak on 05/03/2017.
//  Copyright © 2017 Alexander Danilyak. All rights reserved.
//

import Foundation
import SwiftyJSON

enum CategoryType: String {
    case generalInfo = "GENERAL_INFO"
    case music = "MUSIC"
    case books = "BOOKS"
    case movies = "MOVIES"
    case trips = "TRIPS"
    case groups = "GROUPS"
    case hashtags = "HASHTAGS"
    case friends = "FRIENDS"
    case sport = "SPORT"
    
    func image() -> UIImage {
        switch self {
        case .generalInfo: return #imageLiteral(resourceName: "general")
        case .music: return #imageLiteral(resourceName: "music")
        case .books: return #imageLiteral(resourceName: "books")
        case .movies: return #imageLiteral(resourceName: "movies")
        case .trips: return #imageLiteral(resourceName: "trips")
        case .groups: return #imageLiteral(resourceName: "groups")
        case .hashtags: return UIImage()
        case .friends: return #imageLiteral(resourceName: "friends")
        case .sport: return #imageLiteral(resourceName: "sport")
        }
    }
    
    func name() -> String {
        switch self {
        case .generalInfo: return "General Information"
        case .music: return "Music"
        case .books: return "Books"
        case .movies: return "Movies"
        case .trips: return "Trips"
        case .groups: return "Groups"
        case .hashtags: return "Hashtags"
        case .friends: return "Friends"
        case .sport: return "Sport"
        }
    }
}

struct Category {
    
    var weight: String
    var categoryType: CategoryType
    
    var intersections: [Intersection] = []
    
    init(json: JSON) {
        self.weight = json["weight"].stringValue
        self.categoryType = CategoryType(rawValue: json["category_type"].stringValue)!
        
        for intersectionJson in json["intersections"].arrayValue {
            intersections.append(Intersection(json: intersectionJson))
        }
    }
}
